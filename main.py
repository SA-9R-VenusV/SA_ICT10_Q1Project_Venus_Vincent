def SKU_generator(e):
    document.getElementById("sku_output").innerHTML = " "
    category = document.getElementById("category").value
    product_name = document.getElementById("product_name").value
    stock_qty = document.getElementById("quantity").value

    clean_cat = "".join(c for c in category if c.isalnum()).upper()[:3]
    clean_name = "".join(c for c in product_name if c.isalnum()).upper()[:3]
    clean_qty = "".join(c for c in stock_qty if c.isdigit())[:2]

    sku = f"{clean_cat}-{clean_name}-{clean_qty}"[:8]

    document.getElementById("sku_output").innerHTML = f"SKU: {sku}"