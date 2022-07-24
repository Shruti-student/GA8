import streamlit as st

def main():
  st.title("Maximum_number")
  html_temp = """
  <div style="background-color:white;padding:12px">
  <h2 style="color:blue;text-align:center;">Streamlit maximum number App <h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  number1 = st.number_input("Enter first number",min_value=-1000000000000.0,max_value=1000000000000.0)
  number2 = st.number_input("Enter second number",min_value=-1000000000000.0,max_value=1000000000000.0)
  number3 = st.number_input("Enter third number",min_value=-1000000000000.0,max_value=1000000000000.0)
  result = None
  if st.button("Find maximum"):
    result = max(number1,number2,number3)
  st.success(f"The largest number is {result}")
if __name__=="__main__":
  main()
