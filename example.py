#!/usr/bin/env python

__author__ = ('Imam Omar Mochtar', ('iomarmochtar@gmail.com',))

import os
from cakap.base import BotBase 
from cakap.decorators import auth, chelp
from cakap.filters import filters
from cakap.utils import Utils

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Example(BotBase):

    @chelp('get first word', [
                {'name': 'word'},
        ])
    def cmd_sayword(self, bot, update, args):
        word = args.get('word')
        return 'your word is {}'.format(word)

    @chelp('get first word and second one must be an integer', [
                {'name': 'first'},
                {
                    'name': 'second',
                    'filters': [filters.NUMBER()]
                }
        ])
    def cmd_multi(self, bot, update, args):
        first = args.get('first')
        second = args.get('second')
        return 'first: {}, second: {}'.format(
                    first, second 
                )

    @auth
    def cmd_secret(self, bot, update):
        return 'only registered username can access this'


    def cmd_username(self, bot, update):
        user_details = Utils.user_details(update)
        username = user_details['username']
        if username:
           return 'Your username is {}'.format(username)
        
        return 'username is not configured in your telegram accout'

    def cmd_hello(self, bot, update):
        return 'just a plain cmd'

if __name__ == '__main__':
    token = 'fjdkfdkfkdjfk' 
    # registered user that allowed sending message to function wrapped with @auth decorator
    users = ['iomarmochtar']
    bot = Example(
            token=token,
            users=users
            )
    bot.main()
