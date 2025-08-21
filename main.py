from flask import Flask, request
import pandas as pd
import ast

app = Flask(__name__)

# Example DataFrame
df = pd.DataFrame({
    "a": [1, 2, 3],
    "b": [4, 5, 6]
})

@app.route("/query_pandas")
def query_df():
    expr = request.args.get("expr", "") 
    
    try:
        result = ast.literal_eval(expr)
        result = df.query(expr)
        return result.to_html() 
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
