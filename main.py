questions = [
["1.Who is Cristiano Ronaldo ?",
"Actor",
"Dancer",
"Businessman",
"GOAT",
4 ],
["2.What is full form of FF ?",
"Fukc Fire",
"Fire Free",
"Free Fire",
"Fire Fly",
3 ],
["3.Richest man in india ?",
"Ambani",
"Adani",
"Birla",
"Nova",
4 ],
["4.Capital of india ?",
"Delhi",
"orissa",
"Goa",
"MP",
1 ],
]

winnings = [10000,30000,60000,120000]
i = 0
for question in questions:
        print(question[0])
        print(f"A. {question[1]}")
        print(f"B. {question[2]}")
        print(f"C. {question[3]}")
        print(f"D. {question[4]}")


        a = int(input("\n*Press 1 for A, 2 for B, 3 for C, 4 for D*\n Enter your answer: "))

        if a == question[5]:
            print("Correct answer!")
            print(f"You have won ₹{winnings[i]}\n")
        else:
            print(f"Wrong answer.\n *The correct answer was {question[question[5]]}*")
        
            break
        i+=1
