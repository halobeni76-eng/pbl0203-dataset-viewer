from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
DATA_PATH = "static/data/titanic.csv"


import math

@app.route("/pbl0203")
def pbl0203():
    df = pd.read_csv(DATA_PATH)
    search = request.args.get("q", "").strip()
    page = request.args.get("page", 1, type=int)
    limit_val = request.args.get("limit", "50")
    
    if search:
        mask = df.apply(
            lambda row: row.astype(str).str.contains(search, case=False).any(), axis=1
        )
        df = df[mask]
        
    total_matches = len(df)
    
    # Handle 'all' logic
    if limit_val.lower() == "all":
        per_page = total_matches if total_matches > 0 else 1
    else:
        try:
            per_page = int(limit_val)
        except ValueError:
            per_page = 50

    total_pages = math.ceil(total_matches / per_page)
    
    # Pagination slicing
    start = (page - 1) * per_page
    end = start + per_page
    paginated_df = df.iloc[start:end]

    return render_template(
        "pbl0203.html",
        columns=df.columns.tolist(),
        rows=paginated_df.values.tolist(),
        total=total_matches,
        query=search,
        page=page,
        total_pages=total_pages,
        limit=limit_val
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
