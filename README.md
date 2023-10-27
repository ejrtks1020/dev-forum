# prototype web app

## dev
```sh
npm run dev
uvicorn main:app --reload --host=0.0.0.0:8000
```

## prod docker compose 
```sh
npm run build
docker-compose up --build -d
```