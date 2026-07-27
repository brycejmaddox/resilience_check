core_questions = [
    "Did a parent or adult in your household ever hit, slap, or physically hurt you in a way that left marks or caused injury, prior to age 18?",
    "Did a parent or adult in your household ever regularly swear at, insult, or put you down in a way that felt threatening, prior to age 18?",
    "Did an adult or someone at least 5 years older ever touch you sexually or attempt/complete any sexual act with you, prior to age 18?",
    "Was there ever a time you didn't have enough food, clean clothes, or someone to protect/take care of you, prior to age 18?",
    "Did you feel that no one in your family loved you, thought you were important, or paid attention to you, prior to age 18?",
    "Did you live with anyone who had a problem with drinking or using drugs, prior to age 18?",
    "Did you live with anyone who was depressed, mentally ill, or attempted suicide, prior to age 18?",
    "Did you witness a parent or adult in your household being pushed, hit, or physically hurt by a partner, prior to age 18?",
    "Did a household member ever go to prison or jail, prior to age 18?",
    "Were your parents ever separated or divorced, prior to age 18?"
]
expanded_questions = [
    "Did you personally experience violence or hardship due to war or conflict prior to age 18?",
    "Have you ever been bullied in school or at home (verbally, physically, digitally) prior to age 18? Bullying refers to a repeated/ongoing pattern rather than a one-time instance.",
    "Have you experienced a period of time where you and your family struggled to meet basic needs (food, water, clothing, shelter) prior to age 18?",
    "Were you place in foster care or have experience extended separation from your family (due to incarceration/military deployment/hospitalization, etc.) prior to age 18?",
    "Have you ever been a victim of racism (been discriminated against based on race, called racial slurs, experienced violence due to race, etc.) prior to age 18?"
]
core_categories = [
    "physical abuse",
    "emotional abuse",
    "sexual abuse",
    "physical neglect",
    "emotional neglect",
    "household substance abuse",
    "household mental illness",
    "witnessed domestic violence",
    "incarcerated household member",
    "parental separation/divorce"
]
collection = []
print("DISCLAIMER: The results of this survey are NOT a diagnosis; rather, they should be used as a helpful guide to navigating your experiences")
for i, question in enumerate(core_questions):
    while True:
            response = input(question).lower()
            if response == "yes":
                value = 1
                break
            elif response == "no": 
                value = 0
                break
            else:
                print("Please respond with a 'Yes' or 'No'")
    my_dict = {"category": core_categories[i], "question": question, "answer": value}
    collection.append(my_dict)
score = 0
for item in collection:
    score += item["answer"]
with open("score_history.txt", "a") as file:
    file.write(f"{score}\n")
print("The following questions are part of the expanded portion of the test. Responses will NOT be recorded toward the ACE score.")
for i in expanded_questions:
    while True:
        response = input(i).lower()
        if response == "yes":
            break
        elif response == "no":
            break
        else:
            print("Please respond with a 'Yes' or 'No'")
if score == 0:
    print( "Your score indicates a low likelihood of ACE")
    print("Just a reminder, these results are NOT a diagnosis.")
elif 1 <= score <= 3:
    print("Your score indicates a moderate likelihood of ACE")
    print("Reminder, these results are NOT a diagnosis. Please seek professional help if necessary.")
elif score >= 4:
    print("Your score indicates a high likelihood of ACE")
    print("While your results are not a diagnosis, given your score it is suggested that you receive help from a professional resource.")
print("Thank you for sharing. Your answers to the expanded questions, while not part of the official ACE score, are also recognized as significant, so know that your experiences are valued. " \
"Should your answers to the expanded questions resonate with you, the 988 hotline and SAMHSA website are useful resources that can get you the help you need.")