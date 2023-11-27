import time

phrase = 'This program was created by Ashwin Konda!'

word_count = len(phrase.split())

while True:
    begin = input('Please type: ' + phrase + '\n' + 'Press enter when ready. ')

    t0 = time.time()
    attempt = input('\n')
    t1 = time.time()
    attempt_time_seconds = t1 - t0
    wpm = str(round((word_count / attempt_time_seconds) * 60, 2))

    if attempt == phrase:
        print('\n' + 'Your WPM: ' + wpm)
    else:
        print('\n' + 'Typed incorrectly. Please try again.')

    tryAgain = input('Try again? (y/n) ')
    if tryAgain != 'y':
        break
