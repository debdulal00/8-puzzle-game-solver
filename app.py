from flask import Flask, render_template, request, jsonify
from solver import bfs, astar

app = Flask(__name__)

def parse_input(s):
    try:
        nums = list(map(int, s.split()))
        if len(nums) != 9 or sorted(nums) != list(range(9)):
            return None
        return tuple(nums)
    except:
        return None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/solve", methods=["POST"])
def solve():
    data = request.json
    puzzle = parse_input(data["puzzle"])
    algo = data["algo"]

    if puzzle is None:
        return jsonify({"error": "Invalid input"}), 400

    if algo == "bfs":
        moves = bfs(puzzle)
    else:
        moves = astar(puzzle)

    if moves is None:
        return jsonify({"solvable": False})

    return jsonify({
        "solvable": True,
        "steps": len(moves),
        "moves": moves
    })

if __name__ == "__main__":
    app.run(debug=True)
