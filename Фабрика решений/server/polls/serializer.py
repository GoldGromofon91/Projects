from django.db.models import Q
from rest_framework import serializers

from polls.models import Poll, Question, QuestionChoice, Answer, Participant

#Сериалайзер опросов
class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('id', 'title', 'description', 'visible')

#Сериалайзер вопросов
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'poll', 'title', 'text', 'type')

#Сериалайзер вариантов вопроса
class QuestionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionChoice
        fields = ('id', 'question', 'title', 'text')

#Сериалайзер ответов
class AnswerSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=False)
    participant_id = serializers.IntegerField(required=False)
    poll_id = serializers.IntegerField(required=True)
    question_id = serializers.IntegerField(required=True)
    choice_id = serializers.IntegerField(required=False)
    answer = serializers.CharField(required=False)

    def validate_answers(self, answer):
        if not self.data:
            raise serializers.ValidationError("Для прохождения опроса, нужно ответить хоть 1 вопрос")
        return self.data

    def save(self):
        part_user_id = 0
        user_id = 0
        if not self.data.get('answer') and not self.data.get('choice_id'):
            raise serializers.ValidationError(" Answer or choice_id must be not null.")
        user = self.context.user
        if user.is_anonymous:
            part_usr = Participant.objects.last()
            if not part_usr:
                part_usr = Participant(participant=1)
                part_usr.save()
            else:
                part_user_id = part_usr.id
                part_usr = Participant(participant=part_user_id + 1)
                part_usr.save()
        else:
            user_id = user.id

        if self.data.get('choice_id') and user_id:
            a = Answer(user_id=user_id,
                       poll_id=self.data.get('poll_id'),
                       question_id=self.data.get('question_id'),
                       choice_id=self.data.get('choice_id'))
            a.save()
        if self.data.get('choice_id') and part_user_id:
            a = Answer(participant_id=part_user_id,
                       poll_id=self.data.get('poll_id'),
                       question_id=self.data.get('question_id'),
                       choice_id=self.data.get('choice_id'))
            a.save()

        if self.data.get('answer') and user_id:
            a = Answer(user_id=user_id,
                       poll_id=self.data.get('poll_id'),
                       question_id=self.data.get('question_id'),
                       answer=self.data.get('answer'))
            a.save()

        if self.data.get('answer') and part_user_id:
            a = Answer(participant_id=part_user_id,
                       poll_id=self.data.get('poll_id'),
                       question_id=self.data.get('question_id'),
                       answer=self.data.get('answer'))
            a.save()

#Сериалайзер ответа если есть PK
class AnswerDetailSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField('get_answers')

    class Meta:
        model = Answer
        fields = ('id', 'participant', 'poll', 'question', 'choice', 'answers')

    def get_answers(self, question):
        author_id = self.context.get('request').parser_context['kwargs'].get('pk')
        answers = Answer.objects.filter(question_id=question.id, participant_id=author_id)
        serializer = AnswerSerializer(instance=answers, many=True)
        return serializer.data

#Сериалайзер опросов включая ответы
class DetailSerializer(serializers.ModelSerializer):
    poll_to_answer = AnswerDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ('poll_to_answer', 'title', 'description', 'started_at', 'visible')
