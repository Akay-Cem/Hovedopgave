from db import app, mysql


def insert_product(title, description, price, section, image_path):
    try:
        with app.app_context():
            cur = mysql.connection.cursor()
            cur.execute("SET NAMES utf8mb4;")
            cur.execute("SET CHARACTER SET utf8mb4;")

            query = "INSERT INTO products (title, description, price, section, image_path) VALUES (%s, %s, %s, %s, %s)"
            values = (title, description, price, section, image_path)
            cur.execute(query, values)

            mysql.connection.commit()
            cur.close()
            return True
    except Exception as e:
        print(f"Error inserting product: {str(e)}")
        return False


if __name__ == "__main__":
    title = "Bornholmder"
    description = "Saftig burger af bornholms kødkvæg med cheddar ost og brioche boller. Kommer med sodavand og pommes frites "
    price = 159
    section = "Populær"
    image_path = "/static/images/burgermenu.jpeg"

    if insert_product(title, description, price, section, image_path):
        print("Product inserted successfully")
    else:
        print("Failed to insert product")
