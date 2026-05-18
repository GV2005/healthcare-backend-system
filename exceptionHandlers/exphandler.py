from fastapi.responses import JSONResponse

async def http_exception_handler(request,exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
                "custom error":exc.detail
        }
    )