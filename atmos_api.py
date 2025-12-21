# Add this function to your helper section
def get_stats():
    conn = sqlite3.connect('cases.db')
    c = conn.cursor()
    # Count occurrences of each action_scope
    c.execute("SELECT action_scope, COUNT(*) FROM case_logs GROUP BY action_scope")
    rows = c.fetchall()
    conn.close()
    return {action: count for action, count in rows}

# Add this route to your Flask app
@app.route('/stats', methods=['GET'])
def stats():
    try:
        data = get_stats()
        total_cases = sum(data.values())
        return jsonify({
            "status": "online",
            "total_processed": total_cases,
            "breakdown": data,
            "system_health": "stable" if total_cases > 0 else "awaiting_data"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

