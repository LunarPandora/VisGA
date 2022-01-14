# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Takahashi Akane
define akane = Character("Akane", color="#e663bc")

# Yoshimura Haru
define haru = Character("Haru", color="#db9a72")

# Kobayashi Yuko
# define yuko = Character("Yuko", color="#43b1e0")

# MC - Tanaka Shirogane
define narrator = Character("")

# The game starts here.

default morale = 0

label start:

    scene bg schoolhall
    with fade

    show akane smile
    akane "Hello there!"
    akane "Welcome to Setsuko High School! Let me introduce myself. My name is Takahashi Akane! Nice to meet you."
    akane "Since you are a new student in this school, it's my duty to show you around!"
    akane "Oh yes! I haven't ask your name yet. What is your name?"

    menu:
        "My name is Tanaka Shirogane, nice to meet you.":
            jump intro_akane_a

        "Why do you want to know who i am? Piss off.":
            jump intro_akane_b

label intro_akane_a:
    $ morale += 100
    show akane excited
    akane "Nice to meet you then, Shirogane! Well then, follow me!"

    scene bg transit
    with fade

    narrator "You followed Akane to your classroom..."

    jump enter_classroom

label intro_akane_b:
    show akane angry
    akane "Hey! How rude! I am just trying to be nice and help you here!"
    akane "Ah, whatever. Well, i can see your name from your name tag anyway."
    akane "Whether you like it or not, you'll have to follow me!"

    hide akane angry

    narrator "Akane grab your hand and pull you forcefully. It certainly hurts..."

    jump enter_classroom

label enter_classroom:
    scene bg classroom
    with fade

    show akane smile

    akane "And here we are! Welcome to our classroom!"
    akane "We gonna have a Literature class after this, so you better get prepared, okay?"
    akane "You can sit there while preparing your books and stuff!"
    
    hide akane smile
    
    narrator "Akane point out the chair on the back of the class and then you go and sit there."

    show akane smile

    akane "Well, here we are!"
    
    hide akane smile

    narrator "You hear the bell's ringing and students go to their class."

    show akane surprised

    akane "Oh, it's already the class time!"

    if morale > 0:

        show akane teasing
        akane "See you later, Shiro!"

    else:

        hide akane surprised
        narrator "Akane left in hurry without saying anything."

    jump intro_haru

label intro_haru:
    scene bg classroom
    with fade

    narrator "The bell rings, and it's your breaktime."
    narrator "You saw someone were coming for you from next row of your desk."

    show haru smile
    haru "Hello there, are you the new student on our class?"

    show haru laugh
    haru "Greetings! My name is Yoshimura Haru, nice to meet you."

    show haru smile
    haru "What is your name?"

    menu: 
        "It's Tanaka Shirogane. Nice to meet you too, Haru.":
            jump intro_haru_a
        "Why would you ask? Piss off, will you?":
            jump intro_haru_b

label intro_haru_a:
    $ morale += 100
    show haru laugh
    haru "Okay then, Shiro."

    show haru smile
    haru "Anyway, do you have time to accompany me to library? I have a book i need to find."
    haru "Consider this as trying to familiarize yourself with our school. It will be great!"

    if morale > 100:
        jump meet_akane_class
    else:
        jump accompany_haru_lib

label intro_haru_b:
    show haru scared
    haru "Okay, okay! Don't need to be so scary, okay? Please calm down."
    haru "I am sorry if i made a mistake. I am just trying to be polite and asking your name."
    haru "I am so sorry! Really really sorry!"

    narrator "Haru were trembling in fear, trying to look away."
    haru "Well, i have to go! Uh, bye!"

    hide haru scared

    narrator "Haru left in hurry, seems like she is really scared."

    if morale > 0:
        jump meet_akane_alt
    else:
        jump bad_ending

label meet_akane_class:
    hide haru smile

    narrator "Right before you and Haru went to the Library, you saw Akane walking to you."

    show haru smile at right
    show akane smile at left

    akane "Hello there you guys! Where are you guys going?"
    
    show haru laugh at right

    haru "Oh, hey there Akane! We were just getting ready to go to the library."

    show haru smile at right
    show akane surprised at left

    akane "Oh, i see. But i just get tasked to show Shirogane around."

    show akane smile at left

    akane "Well, what do you think, Shiro?"

    menu:
        "I think i'll follow Akane.":
            jump follow_akane
        "I think i'll follow Haru":
            jump follow_haru

label meet_akane_alt:
    narrator "You walked into corridor, and then suddenly you meet Akane."

    show akane smile
    akane "Hi again, Shiro!"

    show akane sad
    akane "I heard from kids that you scared Haru away."

    show akane angry
    akane "You should apologize to her next time you meet her! Don't be rude to other people."

    show akane sad
    akane "Seriously... it's your first day, too."

    show akane smile
    akane "Nevermind, i am sure you will change to a better person."
    akane "Well then, how about we go to cafeteria? I remember that i have to show you around the school, right?"
    akane "Let's go!"

    jump accompany_akane_cafe

label follow_akane:
    $ morale -= 100
    
    akane "Well, if you said so. Let's go follow me then!"

    show akane blush at left
    akane "Sorry Haru, i'll have to take him to another place!"

    haru "No, no. It's okay Akane. I'll go by myself then. Have fun, both of you!"
    
    hide akane blush
    hide haru smile

    narrator "You said sorry to Haru and then followed Akane."
    jump accompany_akane_cafe

label follow_haru:
    
    show haru ask at right
    haru "You sure? I think you should just follow Akane. She is the one who's tasked to accompany you afterall."

    show akane relaxed at left
    akane "It's okay Haru. I think he's more comfortable with you."

    show akane smile at left
    akane "After all, it's the same whether you or me that accompany him to show him around."

    show haru smile at right
    haru "Okay then, if you insist. Let's go then, Shiro!"
    haru "Take care, Akane! See you later!"

    hide akane smile
    hide haru smile

    narrator "You said sorry to Akane and then followed Haru."
    
    jump accompany_haru_lib

label accompany_akane_cafe:
    scene bg transit
    narrator "You and Akane then walk..."

    scene bg cafeteria
    narrator "You finally arrived at Cafeteria. A big one, it seems."

    show akane talk
    akane "And here we are! Welcome to the Cafeteria. You can buy some snacks and drinks in here."

    show akane teasing
    akane "Let's get some, shall we? My treat, hehe."

    hide akane teasing

    narrator "You both then have a lunch together at Cafeteria. After that..."

    jump ending_akane

label accompany_haru_lib:
    scene bg transit
    narrator "You and Haru walk to the library together."

    scene bg library
    with fade

    show haru smile
    haru "Well here we are!"
    haru "Thanks for accompanying me anyway. Oh yeah, i need to find my book now. Let's go!"

    hide haru smile

    narrator "You both then try to find the book. After that..."

    jump ending_haru

label ending_akane:
    scene bg transit
    with fade

    narrator "4 years later..."

    scene bg ending_akane
    with fade

    akane "You're late, honey."

    narrator "You hear someone that seems familiar. You turn around and see Akane standing in front of you."

    show akane ending
    
    akane "Hello there honey! I've been waiting for you, hehe."
    akane "Today i have some time off from my office! I want to enjoy this holiday and spend time with you, hehe."

    show akane ending_1
    narrator "Akane then stand beside you and hug your hand tight."

    show akane ending_2
    akane "Let's go have some walk together, shall we?"

    hide akane ending_2
    narrator "The End."

    return

label ending_haru:
    scene bg transit
    with fade

    narrator "4 years later..."

    scene bg ending_haru
    with fade

    haru "Hey! Over here Shiro!"

    narrator "You are walking around and then see someone familiar."
    narrator "You then walk towards that person. She seems so happy to see you."

    show haru ending

    haru "Hi there Shiro!"
    haru "Finally, we meet again after graduation. It's been so long, isn't it?"
    
    narrator "Both of you stood silently... reminiscing the old good memories."

    haru "Actually... i've been waiting this day."
    haru "I actually want to tell you something... that I..."

    narrator "You looked at her. Standing silently, waiting for something she wants to tell you after so long..."

    show haru ending_2
    haru "..."

    show haru ending
    haru "I love you."
    haru "Thank you for being so nice for me after all this time. Thank you for staying by my side."

    hide haru ending
    narrator "The End."

    return

# label intro_yuko:
# label ending_yuko:

label bad_ending:
    scene bg transit
    
    narrator "Since then... you always have been rude to other people."
    narrator "All students on your school have also heard about how rude you are to Akane and Haru."
    narrator "..."

    narrator "Do you even feel any kind of guilt or remorse?"

    return