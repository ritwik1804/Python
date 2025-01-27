questions = [
    ["Grand Central Terminal, Park Avenue, New York is the world's", 
"largest railway station", "highest railway station", "longest railway station", "None of the above", 1],
["Entomology is the science that studies", "Behavior of human beings", "Insects", 
"The origin and history of technical and scientific terms", "The formation of rocks", 2 ],
["Eritrea, which became the 182nd member of the UN in 1993, is in the continent of", "Asia", 
"Africa", "Europe", "Australia", 2],
["Garampani sanctuary is located at", "Junagarh, Gujarat", "Diphu, Assam", 
 "Kohima, Nagaland", "Gangtok, Sikkim", 2],
["For which of the following disciplines is Nobel Prize awarded?", "Physics and Chemistry", 
"Physiology or Medicine", "Literature, Peace and Economics", "All of the above", 4],
["Hitler party which came into power in 1933 is known as", "Labour Party", 
"Nazi Party", "Ku-Klux-Klan", "Democratic Party", 2],
["FFC stands for", "Foreign Finance Corporation", "Film Finance Corporation", 
 "Federation of Football Council", "None of the above ", 2],
["Fastest shorthand writer was", "Dr. G. D. Bist", "J.R.D. Tata", "J.M. Tagore", 
 "Khudada Khan", 1],
["Epsom (England) is the place associated with", "Horse racing", "Polo", "Shooting"
 , "Snooker", 1],
["First human heart transplant operation conducted by Dr. Christiaan Barnard on Louis Washkansky, was conducted in", 
 "1967", "1968", "1958", "1922", 1],
["Galileo was an Italian astronomer who", "discovered that the movement of pendulum produces a regular time measurement", 
"developed the telescope", "discovered four satellites of Jupiter", "All of the above", 4],
["Habeas Corpus Act 1679", "states that no one was to be imprisoned without a writ or warrant stating the charge against him", 
"provided facilities to a prisoner to obtain either speedy trial or release in bail", "safeguarded the personal liberties of the people against arbitrary imprisonment by the king's orders"
, "All of the above", 4],

]

levels = [1000, 2000, 5000, 10000, 20000, 40000, 160000, 640000, 1250000, 2500000, 5000000, 10000000]
money = 0
for i in range(0, len(questions)):
    q= questions[i]
    print(f"\n\n Question for Rs. {levels[i]}")
    print(f"Q: {q[0]}")
    print(f"a. {q[1]}    b. {q[2]}")
    print(f"c. {q[3]}    d. {q[4]}")
    reply = int(input("Enter your number (1-4)"))
    if(reply == q[-1]):
        print(f"Correct ans, you have won Rs. {levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 8):
            money = 320000
        elif(i == 12):
            money = 10000000
    else:
        print("Wrong answer")
        break
print(f" Your take home money is {money}") 
