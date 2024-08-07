let i;

document.getElementById('downloadButton').addEventListener('click', async function() {
    let url = document.getElementById('videoUrl').value;
    let filename;
    for(i =2;i<=100;i++){
         filename = 'video_filename'+i; 
        i++;
        break;
    } // You can also allow the user to input this

    if (url) {
        try {
            const response = await fetch('http://127.0.0.1:8000/download/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ url: url, filename: filename }),
            });

            if (response.ok) {
                const data = await response.json();
                console.log('Response:', data);
                alert(data.message);
            } else {
                const errorData = await response.json();
                console.error('Error Response:', errorData);
                alert('Failed to receive valid response: ' + (errorData.detail || 'No details available'));
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to send request');
        }
    } else {
        alert('Please enter a video URL');
    }
});
