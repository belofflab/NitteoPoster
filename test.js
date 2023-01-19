const data = { username: 'example' };

fetch('https://example.com/profile', {method: 'POST',headers: {'Content-Type': 'application/json',},body: JSON.stringify(data),})