const BASE_URL = import.meta.env.VITE_SERVER_URL; // API 서버의 기본 URL

// HTTP GET 요청을 수행하는 함수
export async function get(endpoint, params = {}) {
  const url = `${BASE_URL}${endpoint}`;

  try {
    const response = await fetch(url, {
      method: 'GET',
    });
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const json = await response.json();
    return json;
  } catch (error) {
    throw new Error(`GET request failed: ${error.message}`);
  }
}

// HTTP POST 요청을 수행하는 함수
export async function post(endpoint, data = {}) {
  const url = `${BASE_URL}${endpoint}`;

  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const json = await response.json();
    return json;
  } catch (error) {
    throw new Error(`POST request failed: ${error.message}`);
  }
}
