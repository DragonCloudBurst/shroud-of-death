# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Cairn", color="#d65d5b")
define m = Character("Makoto", color="#e4439c")


transform left:
    xalign 0.1 yalign 1.0

transform right:
    xalign 0.9 yalign 1.0

transform makoto_size:
    zoom 1.3

# The game starts here.

label start:

    scene forest

    "Sometimes, even gods feel aimless."
    "In a remote forest in Hokkaido, a lone deity wanders down their well-worn paths in silence."
    "If a mortal were to see them, would they likely think the god was pacing and fretting... but the divine beast would never admit that."

    show cairn_normal at left 

    c "Sometimes I wonder why I bother."
    "Cairn kicks a pebble on the ground absentmindedly, and it skitters off into the weeds."
    c "It's not like I'm ever shown any appreciation for my duties, is it? None of the creatures here know what I do. They know not how
    many threats and dangers I ward off."

    hide cairn_normal
    show cairn_worried at left

    c "Sometimes I wonder what shall happen if I were to leave and never return. Would my people even notice?"
    "A gust of wind blows through the leaves of the trees above the god, snapping them back to reality."
    c "What nonsense am I saying? I must stay. I have no other choice to make."
    c "I suppose that, from time to time, I just wish that they would acknowledge my work for them. But, then again... that may require revealing
    information to the locals that is not already known."
    c "There really is not a good answer."
    pause 1.0
    "Suddenly, the snap of a twig rings out through the area, and Cairn whirls around to see what could have made the noise."

    hide cairn_worried
    show cairn_shocked at left

    c "Halt! Who goes there?"
    "Cairn glances around wildly for several moments before their eyes finally come to rest on a lady in a yukata picking flowers."
    "The deity relaxes a bit. It's just a human- and an elderly one at that."

    hide cairn_shocked
    show cairn_normal at left

    c "Who are you? Why are you here?"
    "The woman looks up from her floral charge and smiles slightly, adjusting her spectacles as if this is an everyday occurence."
    pause 1.0 

    show makoto_smile at right, makoto_size
    
    m "My name is Makoto. It is nice to meet you."
    "She smiles slightly, and the skin near her eyes wrinkles as she does so."
    m "I really should be asking you who you are, too. I've never met you before, and as far as I know, you could be a threat to me."

    hide cairn_normal
    show cairn_worried at left

    c "Do you really not know who I am?!"
    c "That's... surprising. I thought all those here knew of me."
    m "I must confess, I have no idea who you are. I apologize."

    hide makoto_smile
    show makoto_worry at right, makoto_size

    m "That... does not upset you, does it?"

    hide cairn_worried
    show cairn_normal at left

    c "That is not so. It simply surprises me. Enraged I am not."
    m "I see."

    hide makoto_worry
    show makoto_shock at right, makoto_size

    m "You are not going to eat me, are you?! I have heard stories of dangers in these parts, but I had never thought them to be true."
    "Cairn scoffs, incredulous."
    c "Such a thing is unfathomable. I am not a killer, nor a predator."
    "They notice that Makoto is shaking a bit in spite of their words, and they sigh."
    c "I will not harm you. I can promise you that."
    c "Why are you still shaking? You have been told to be calm."
    pause 1.0
    "The elderly woman shudders a bit and takes a deep breath to slow her thoughts."
    m "I apologize. I am just nervous. I have never met anyone like you before."
    m "I am not sure what to think of you."
    "Cairn nods slowly, yet still feels a bit slighted. They are not used to their commands not being immediately obeyed."
    "Then again, they aren't used to humans, either."
    c "Is it really so common for beasts to speak as I do? You do not seem to be put off guard by that in particular."
    "Makoto hesitates for a moment."

    hide makoto_shock
    show makoto_worry at right, makoto_size

    m "I have not seen it before myself, but my fellow miko have told me of such things occurring. I trust them with my life, so I would never
    doubt their word."
    c "...I see."
    "Cairn's tail swishes impatiently as they consider what to do next. They could just leave... but that doesn't seem like the right thing to do."
    "Before they can finish deliberating, Makoto spares them the need to make a concrete deicision."
    m "If you would like, you may walk back with me to our shrine. I have some tea that I could make for you. Tea is... a measure of gentility."
    m "However, if you do not wish to have any, I will not hold it against you."
    "Cairn blinks once, then twice. No one had ever invited them to visit, much less a human, much less for a serving of tea. The absurdity of the moment
    almost silences them."

    hide cairn_normal
    show cairn_happy at left

    c "I accept."

    hide cairn_happy
    hide makoto_worry
    scene gazebo with fade 
    pause 2.0
    show cairn_normal at left

    ###############################
    # scene 2 start
    ###############################
    c "I appreciate the invitation. I have never been offered something like this before."

    show makoto_smile at right, makoto_size

    m "Really? Never? That is surprising."
    "Cairn huffs."
    c "You must understand that this is far from my usual activities."
    m "Well, what are your usual activities? Care to tell me?"
    "Cairn goes quiet."
    c "I cannot tell you."
    "Makoto sighs as she prepares the tea."
    m "I cannot force you to tell me anything. I respect privacy."
    "The pair are silent for several moments while the tea soaks. Makoto is the first to speak."
    m "Have you ever had matcha before?"
    c "What is this 'matcha' you speak of?"
    "Makoto laughs softly in spite of the tension in the air. She picks up the teapot and carefully serves a small portion of the drink into two cups-
    one for herself and one for Cairn."
    m "It is a form of tea, often used for ceremonies. I apologize that I do not have any other type of tea on hand. Matcha can be a bit overwhelming
    if you have never drank it before."
    c "I can handle myself. Worry not."
    m "I see. Then, here is your cup."
    "Makoto begins taking small sips from her cup, as Cairn dives their snout in and takes a huge gulp all at once."
    
    hide makoto_normal
    show makoto_shock at right, makoto_size

    m "Oh, that's- You are not supposed to-"

    hide cairn_normal
    show cairn_shocked at left

    "Before she can finish her warning, Cairn reels back, coughing violently."
    m "I told you it was strong..."
    "Cairn hacks and sputters, trying to regain their composure."

    hide cairn_shocked
    show cairn_worried at left

    c "It's... lovely. The flavor is quite... unique."
    "They cough again, and their voice sounds strained."
    c "It is hotter than I aniticipated."

    hide makoto_shock
    show makoto_worry at right, makoto_size

    m "Are you okay? I can get you some clean water if needed."
    c "No, no. I am fine. I am alright."
    "Cairn shakes their body, causing their fur to fluff out. They clear their throat and take a seat once more."
    m "If you wish to try some more, take small sips. Do not drink it all at once. It is very hot and has a strong taste."
    c "...Right. I knew that."
    c "With their pride bruised, Cairn delicately leans down and takes a much smaller mouthful of the matcha. They pause for several moments,
    then swallow it down."

    hide cairn_worried
    show cairn_happy at left

    c "It is... quite nice when I drink it like this."
    "Cairn almost can't believe what they're about to say, but they say it anyway."
    c "Thank you very much."

    hide makoto_worry
    show makoto_smile at right, makoto_size

    m "I'm quite glad you like it. I apologize for not warning you sooner; I thought you would know."
    "If Cairn could blush in embarassment, they would. Instead, their tail twitches back and forth."
    c "I did know. Clearly."
    "Makoto smiles softly."
    m "Right. Of course you did."

    hide cairn_happy
    hide makoto_smile
    scene shrine with fade
    pause 2.0
    show makoto_smile at right, makoto_size

    ###############################
    # scene 3 start 
    ###############################

    m "I am surprised that you came again, but I am happy for it."
    m "I never did get your name. Do you mind telling me?"

    show cairn_normal at left

    "The deity hesitates before giving their answer."
    c "I am... Cairn. It is not my true name, yet it is the only somewhat-accurate version that can be pronounced by humans."
    "Makoto nods slowly."
    m "I see. Ca... Cairn."

    hide makoto_smile
    show makoto_worry at right, makoto_size

    "She stumbles over the syllables a bit, and looks noticeably embarassed."
    m "That is not a Japanese name. Are you not from here?"

    hide cairn_normal
    show cairn_worried at left

    "Cairn starts to get the feeling that Makoto may know more than she lets on."
    c "That is hard to answer. I cannot say yes, nor can I say no. It is... complicated."
    m "I apologize. I have intruded."
    c "No, it is alright. It is a reasonable question."
    "Cairn sighs softly."
    c "I wish I could tell you more, Makoto."
    "Makoto shrugs, shaking her head."

    hide makoto_worry
    show makoto_smile at right, makoto_size

    m "It is alright. I am okay with not knowing everything."
    "A faint feeling of guilt gnaws at Cairn even so."
    m "Come, I would like to show you our gardens. Walk with me, if you do not mind?"

    hide cairn_worried
    show cairn_happy at left

    c "I would very much like to."
    
    pause 2.0

    "Makoto leads Cairn down a path off to the side of the shrine, and they follow her with vague caution."
    m "Look, Cairn. Is it not quite pretty?"
    "Cairns looks to follow Makoto's gaze, and their jaw nearly drops at the sight."

    hide cairn_happy
    show cairn_shocked at left

    "The flowers are stunning, yes, but what really catches their interest is one of the statues that they can see from here."
    "The stone sculpture is a very clear and unmistakable representation of their mentor."
    "How was this possible? Cem was well-known among the gods for being reclusive and antisocial, even more so than themself."
    "So how do these humans know of its existence, much less have created a strikingly accurate statue of it?"
    
    hide makoto_smile
    show makoto_worry at right, makoto_size

    m "Are you alright? You look as though you have seen an obake. Should I be worried?"

    hide cairn_shocked
    show cairn_worried at left

    c "I... I am fine. Do not worry about me. Just... the flowers are very beautiful. It has been a long time since I have seen such beauty
    in human territory."
    "Makoto nods. The gleam in her eyes shows she seems to have the inkling that Cairn isn't telling the full truth, but she doesn't press the matter."
    
    hide makoto_worry
    show makoto_smile at right, makoto_size

    m "I am very glad you like our humble garden. We do not have much, but we miko take great pride in caring for our garden."
    c "It is very lovely and well-tended. I am used to seeing flowers, but I am not used to seeing such neat and tidy plants."
    "Makoto's smile widens."
    m "That is great to hear. It makes me happy to know that you can appreciate our hard work."
    "Despite their lingering shock, Cairn nods and tilts their head forwards in acknowledgement."

    hide cairn_worried
    show cairn_happy at left

    c "Thank you very much for showing me, Makoto. I appreciate it."
    "The pair stand in silence for a while, simply admiring the flowers."
    "In moments like these, time seems to stand still."

    hide makoto_smile
    hide cairn_happy
    scene gazebo with fade
    pause 3.0

    ###############################
    # scene 4 start 
    ###############################

    show cairn_happy at left
    show makoto_smile at right, makoto_size

    m "It is lovely to see you again, Cairn."
    m "It wasn't long since your last visit. You typically visit once a week or so, but I just saw you two days ago."
    m "To see you again so soon is a surprise, but a pleasant one."
    c "Yes, well... if I'm being honest, I've been a little lonely lately, and I wanted to see you again. I don't have many others to talk to."
    m "Well, I'm glad we're friends then."
    m "But, I have a sense that is not the only reason you've come, is it?"

    hide cairn_happy
    show cairn_worried at left

    c "How could you tell?"
    m "I have become more perceptive with age. You do not get to 67 years of life without being at least a little wise."
    c "Well... you are correct. I wanted to let you know that I have seen some unrest near the forest within the past. It's some kind of human group.
    They were yelling amongst themselves and seemed excited, but their intentions did not seem well. They spoke in a tongue I did not recognize;
    I expect it may have been a form of secret code. Even the sight of them brought unease upon me."
    c "I believe you and the other miko should be very careful for the next few days. They were carrying weapons."
    c "I fear for your safety, and the safety of the forest as a whole."

    hide makoto_smile
    show makoto_worry at right, makoto_size

    "Makoto is silent for several moments."
    m "I understand why you are concerned about this."
    m "I believe I have heard of a similar group before a couple of years ago. But, nothing ever came of it."
    m "You are a little too worried, I think, but I appreciate the warning."
    m "Not many outsiders even know our shrine is here. This location was chosen for us for a reason: its seclusion and safety."

    hide makoto_worry
    show makoto_smile at right, makoto_size

    m "Now, I do happen to have some leftover teriyaki soba from our lunch earlier. Would you like some?"
    m "I saved it just in case you stopped by."

    hide cairn_worried
    show cairn_happy

    c "I'd love to partake."
    c "You're correct. I do worry too much. But at least I can rest easy in that you have been alerted."
    m "It's not good to worry too much, but it is good to look out for the safety for others. All in moderation."
    m "Here, I will go fetch the soba. Wait for me here."

    hide cairn_happy
    hide makoto_smile
    pause 3.0


    ###############################
    # scene 5 start
    ###############################





    # This ends the game.
    return
