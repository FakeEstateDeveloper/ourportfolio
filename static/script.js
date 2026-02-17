// Load all existing items
async function LoadItems() {
    const data = await fetch("/items");                     // Fetch the data from the server
    const parsedData = await data.json();                   // Parse the JSON data into JS array
    
    const list = document.getElementById("item-list");      // Gets the <ul> element from HTML
    list.innerHTML = "";                                    // Clears the current list

    parsedData.forEach(element => {                         // Loops over every item in the data array
        const li = document.createElement("li");            // Creates a new list item <li></li>
        li.textContent = element.ToDo;                      // Sets the text into the <li></li>
        list.appendChild(li);                               // Inserts the current <li> into the <ul>
    });
}

// Adds an item
async function AddItem() {
    const input = document.getElementById("todo-input");    // Gets the <input> element from HTML
    const text = input.value;                               // Gets the current text <input>'s value

    if (!text) return;                                      // If no text then do nothing

    const data = await fetch("/item", {                     // POST to /item
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ ToDo: text })
    });

    input.value = "";                                       // Clears the <input> value
    LoadItems();                                            // Reload all existing items
}

// Removes the item from the list when clicked on
async function Remove() {}

// load items when page opens
LoadItems();