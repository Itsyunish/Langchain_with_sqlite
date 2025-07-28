from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st 
import sqlite3

#Loading the enviornment varibale
load_dotenv()

# function to load google gemini model and provide sql query as response
def get_gemini_response(question,prompt):
    model = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash")
    response = model.invoke("question: " + question + "\n" + prompt)
    return response.content
    
    
# function to retrieve dara from sqlite database
def read_sql_query(sql, db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()

    return rows

# defining my prompt
prompt = """
You are an expert in converting English questions to SQL query ! The SQL database has the name STUDENT and has the following columns: NAME, CLASS, SECTION, ROLL_NO, MARKS \n For example, \n Example 1 - How many entries of record are present ?, SQL command for this will be something like this: SELECT COUNT(*) FROM STUDENT; \n Example 2 - What is the name of the student with roll number 1 ?, SQL command for this will be something like this: SELECT NAME FROM STUDENT WHERE ROLL_NO = 1; \n Example 3 - What is the class of student with roll number 2 ?, SQL command for this will be something like this: SELECT CLASS FROM STUDENT WHERE ROLL_NO = 2;   

also the sql code should not have ``` in the beginning or end and sql word in output
"""

# Streamlit app

st.title("GoogleGemini SQL Query Generator")
st.header("Ask a question to generate SQL query")

question=st.text_input("Input", key="input")

submit = st.button("Ask a question")

if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response, 'Student.db')
    st.subheader("SQL Query Result")
    for row in data:
        print(row)
        st.header(row)


