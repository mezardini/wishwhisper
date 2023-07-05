const cartItems = [
    { name: "Item 1", quantity: 2, price: 10 },
    { name: "Item 2", quantity: 1, price: 5 },
    { name: "Item 3", quantity: 3, price: 15 },
  ];
  
  const totalPrice = cartItems.reduce((total, item) => total + item.quantity * item.price, 0);
  
  const requestBody = {
    items: cartItems,
    totalPrice: totalPrice,
  };

  

  


  fetch('http://127.0.0.1:8000/api/cart/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(requestBody),
  })
    .then(response => {
      // handle the response from the API
    })
    .catch(error => {
      // handle any errors that occurred
    });
  