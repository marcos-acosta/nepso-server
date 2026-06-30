from fastapi import FastAPI, Request, Response
from nepso import Printer, Text, CutAndPrint

app = FastAPI()


@app.post("/print")
async def print_text(request: Request):
    body = (await request.body()).decode("utf-8")
    with Printer() as printer:
        printer.execute(
            [
                Text(body + "\n"),
                CutAndPrint(),
            ]
        )
    return Response(status_code=204)


def main():
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
