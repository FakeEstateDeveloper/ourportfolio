// Load all existing items
async function LoadItems() {
    const response = await fetch("/items");                 // Fetch the data from the server
    const data = await response.json();                     // Parse the JSON data into JS array
    
    const list = document.getElementById("item-list");      // Gets the <ul> element from HTML
    list.innerHTML = "";                                    // Clears the current list

    data.forEach(element => {                               // Loops over every item in the data array
        const li = document.createElement("li");            // Creates a new list item <li></li>
        li.textContent = element.ToDo;                      // Sets the text into the <li></li>
        list.appendChild(li);                               // Inserts the current <li> into the <ul>
    });
}

// Adds an item
async function AddItem() {
    const input = document.getElementById("todo-input");
    const text = input.value;

    if (!text) return;

    await fetch("/item", {                                  // POST to /item
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ ToDo: text })
    });

    input.value = "";
    LoadItems();                                        // refresh list
}

// load items when page opens
LoadItems();