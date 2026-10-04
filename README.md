# # MIS203 Basic Programming

* *Name:* Irmak Sütkesin
* *Student Number:* 2404109061
* *Department:* Management Information Systems
* *Course Name:* Basic Programming

---
# # Week 01
* *AI Tool Used:* Gemini
* *Prompt Used:* "Write a Python script that asks for Name, Department, Age, and Career Goal, then prints a formatted Student Profile."
* *What did you change?:* I customized the prompt parameters and formatted the profile display to meet assignment requirements.


---

# # Week 02
* AI Tool Used: Gemini
* Prompt Used: "How can ı write this code?"
* What did you change? I reviewed the code, matched the output format to the example and checked the average calculation.
* What does break do in your program? The break statement stops the loop when the user types 'q', so the program can calculate and print the average.


  ---

  # # Week 03
  * AI Tool Used: Gemini,ChatGPT
  * Prompt Used: "Could you explain the logic of this code to me?"
  * What did you change?: I used `.strip().lower()` for robust input handling and formatted float outputs to 2 decimal places with f-strings.
  * Tests:
   - Age = 3, Day = weekday, Student = no => Output: Olivia: 0.00 TRY (free)
   - Age = 21, Day = weekend, Student = yes => Output: John: 175.00 TRY (student)
   - Age = 8, Day = weekday, Student = no => Output: Illy: 120.00 TRY (child)
  * Why does the order of the rules matter?: If the Student rule comes before the Child rule, a 10-year-old student would match the Student condition first and       get a 30% discount instead of the better 40% Child discount.
