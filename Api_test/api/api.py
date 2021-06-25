from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

expected_sortBy_value_set = {"id","reads","likes","popularity"}
expected_direction_value_set = {"asc", "desc"}

@app.route("/api/ping")
def ping():
    resp = {"success": True}
    return jsonify(resp), 200

@app.route("/api/posts/")
def posts():
    tag_str = request.args.get("tags")
    if tag_str == None:
        return {"Error": "Tags parameter is required"}, 400

    sortBy_str = request.args.get("sortBy")
    sortBy = sortBy_str if sortBy_str != '' else "id"
    if sortBy not in expected_sortBy_value_set:
        return {"Error": "sortBy parameter is invalid"}, 400
    
    direction_str = request.args.get("direction")
    direction = direction_str if direction_str != '' else "asc"
    if direction not in expected_direction_value_set:
        return {"Error": "direction parameter is invalid"}, 400
    
    tags = tag_str.split(",")
    posts = []
    for tag in tags:
        blog = requests.get(
                        f"https://hatchways.io/api/assessment/blog/posts?tag={tag}"
                    ).json()
        posts += blog["posts"]
    print(posts)
    post_ids = set()
    filtered_posts = []
    for p in posts:
        if p['id'] not in post_ids:
            filtered_posts.append(p)
            post_ids.add(p['id'])

    direction_val = True if direction == "desc" else False   
    sorted_data = sorted(filtered_posts, key=lambda x : x[sortBy], reverse=direction_val)
    return jsonify({"posts": sorted_data})

if __name__ == "__main__":
    app.run()