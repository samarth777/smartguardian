document.addEventListener('DOMContentLoaded', function() {
    // Example function to simulate receiving data from the server
    function receiveDataFromServer() {
        fetch('http://localhost:5000/capture')
            .then(response => response.json())
            .then(data => {
                var old = data.image_url;
                var newPath = old.replace("./main/", "./");
                document.getElementById('carImage').src = newPath;
                console.log(newPath)
                document.getElementById('carDescription').textContent = data.description;
            })
            .catch(error => console.error('Error fetching data:', error));
    }
    
    // Call the function to fetch data from the server
    receiveDataFromServer();

    // Example function to handle arrow button clicks
    function handleArrowClick(direction) {
        console.log(`Car moving ${direction}`);
        fetch(`http://10.1.1.205?control=${direction}`)
        .then(response => {
            if (!response.ok) {
              throw new Error('Network response was not ok');
            }
            return response.json(); // This returns a promise
          })
          .then(data => {
            console.log(data); // Here you can handle the data from the response
          })
          .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
          });
        // Here, you would typically send a request to the server to control the car
    }

    // Add event listeners to the arrow buttons
    document.getElementById('leftArrow').addEventListener('click', () => handleArrowClick('left'));
    document.getElementById('upArrow').addEventListener('click', () => handleArrowClick('up'));
    document.getElementById('rightArrow').addEventListener('click', () => handleArrowClick('right'));
    document.getElementById('downArrow').addEventListener('click', () => handleArrowClick('down'));
});
