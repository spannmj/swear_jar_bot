import praw
from config import config
import sqlite3 as lite
import sys


def get_comments_for_user( user_name, reddit ):
    # this fuction returns all the comments for a user
    reddit_user = reddit.get_redditor(user_name)
    comments = reddit_user.get_comments()
    return comments


def main():

    swear_words = ['fuck', 'shit', 'bitch', 'cunt', 'asshole']

    r = praw.Reddit(user_agent=config['user_agent'])
    r.login(config['username'], config['password'])

    # Get all comments
    all_comments = r.get_comments('all')

    # Get comments for testing
    for comment in all_comments:
        if any(s in comment.body.lower() for s in swear_words):
            user = comment.author
            swear_comment = comment.body
            print "This dude swore: %s" % user

            # Connect to DB
            con = lite.connect('test_sinners.db')
            #with con:
            cur = con.cursor()
            cur.execute('INSERT INTO comments VALUES(NULL,"{0}","{1}",0)'.format(user, swear_comment))

            cur.execute('SELECT COUNT(*) FROM comments WHERE user = "{}"'.format(user))
            con.commit()
            swear_count = cur.fetchone()[0]

            if swear_count <= 1:
                print "New user: %s" % user

                # comment.reply('You just swore! Repent for your sins at [swearjarbot.com](swearjarbot.com/?user=%s).') % author


            ### User exists, need to update ###
            else:
                print "Existing user: %s \nOld swear count: %s" % (author, swear_count)

                # comment.reply('You just swore! I've caught you %s times. Repent for your sins at [swearjarbot.com](swearjarbot.com/?user=%s).') % (swear_count, author)


            # Close connection - Not sure when the fuck to close this connection.
            #    con.close()

if __name__ == '__main__':
    main()
