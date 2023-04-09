from datetime import datetime
from rest_framework import serializers



class Comment:

    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()


comment = Comment(email='leila@example.com', content='foo bar')

serializer = CommentSerializer(comment)
serializer.data

breakpoint()