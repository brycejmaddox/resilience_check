# Resilience Check

*DISCLAIMER: The results of this survey are NOT a diagnosis; rather, they should be used as a helpful guide to navigating your experiences.*

## Purpose

This tool serves as a means of personal reflection for users, with its questions being built around the CDC-Kaiser ACE framework. By asking ACE-indicator questions, users can both better understand how past experiences may've affected them, as well as receive helpful resources to help them navigate their experiences.

## Features

* Separation of the 10 core questions of the test and the 5 expanded questions. The expanded questions do not count towards the score calculated in order to maintain the valid scoring bands.
* Input validation (yes/no responses only accepted) and re-prompting when input is invalid.
* The user receives a score interpretation based on the scores received from their answers to the core questions.
* At the end of the test the user will receive resources they can refer to if need be.

## Ethical Considerations

The questions asked in the survey were developed from published research (the CDC-Kaiser ACE study, the Philadelphia ACE Project), which is why I chose them. Ensuring that the test itself is valid in all aspects was imperative. I also chose to remind the user that the results of the test were not a diagnosis. Because I am not a licensed psychologist, I have no grounds to make definitive statements about another's mental wellbeing. Another important concern I'd like to touch on is the separation of validated and expanded questions. The expanded questions served a solely exploratory purpose, simply as a means of personal reflection. Since the typical ACE test only contains 10 questions, it was important that I distinguish the extra 5 questions from the core 10 ones. Since the scoring bands on the validated 10-question format are 0/1-3/4+, including the expanded questions in the scoring would've made the results essentially meaningless.

## Concepts Used

* Lists for storing questions and values for users' answers
* for loops to subsequently ask questions and record responses
* while/nested loops to ensure input validation (only yes/no responses)
* if/elif/else conditionals to decide value to append to answer list and prevent input invalidation
* Comparison operators (including chained comparisons) to interpret scores
* string methods (.lower()) to reduce case sensitivity
* built in functions (sum()) to calculate scores from lists
* input() and type/format handling to translate answers into numerical scores

## Personal Note

I created this tool for more than just as a way to gain more experience with coding. At the time of the tool's creation, I was a psychology major and wanted to find a way to incorporate my interest in psychology with computer science in a meaningful way. Since Adverse Childhood Experiences (ACE) are a very sensitive topic that holds significant, personal value to me, I understand that completing tests like this can be difficult for some.

Regardless of whether or not you are comfortable dealing with childhood trauma, simply confronting and acknowledging it is a meaningful start to the journey of healing. Because of that, I hope that I can expand upon this tool so that it can reach the lives of others who may relate to its significance.