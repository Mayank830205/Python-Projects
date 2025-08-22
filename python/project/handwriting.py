# import pywhatkit as pw

# txt="Introduction: Python is a high-level, interpreted programming language known for its simplicity and readability.Syntax: Python uses indentation instead of curly braces to define code blocks."


# pw.text_to_handwriting(txt, "C:\\Users\\HP\\Desktop\\python\\project\\handwriting.py\\demo1.png", (0, 0, 138))



# print("END ")

import pywhatkit as pw
#pw.search("whatapp")

txt = "Introduction: Python is a high-level, interpreted programming language known for its simplicity and readability. Syntax: Python uses indentation instead of curly braces to define code blocks."

#pw.text_to_handwriting(txt)
pw.text_to_handwriting(txt, "text.png", (255, 0, 0))  # Red color


print("END")
