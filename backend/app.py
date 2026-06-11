# Inside backend/app.py, update the router inclusion block:
from routers.auth import router as auth_router

app.include_router(health_router, prefix="/api/v1")
app.include_router(auth_router, prefix="/api/v1") # Added auth routing
app.include_router(ai_router, prefix="/api/v1")
)

# Request-response interception middleware to calculate operational times
@app.middleware("http")
async def process_telemetry_metrics(request: Request, call_next: Callable) -> Response:
    start_time = time.time()
    logger.info(f"Processing inbound connection state: {request.method} {request.url.path}")
    try:
        response = await call_next(request)
        duration = (time.time() - start_time) * 1000
        response.headers["X-Process-Time-Ms"] = f"{duration:.2f}"
        logger.info(f"Successful runtime transaction: {request.method} {request.url.path} handled in {duration:.2f}ms")
        return response
    except Exception as exc:
        duration = (time.time() - start_time) * 1000
        logger.error(f"Critical execution error caught on framework pipeline: {str(exc)} after {duration:.2f}ms", exc_info=True)
        raise exc

# Global error exception parsing to abstract backtrace arrays from escaping to production users
@app.exception_handler(Exception)
async def catch_unhandled_system_exceptions(request: Request, exc: Exception) -> JSONResponse:
    logger.error(f"Global application barrier caught anomalous exception event: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "error": "InternalServerError",
            "message": "An unhandled issue was met while managing elements inside the Ronex AI processing thread framework."
        }
    )

# Inject structural network API routing domains
app.include_router(health_router, prefix="/api/v1")
app.include_router(ai_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    logger.info(f"Launching Ronex AI processing application on production environment stack: {settings.HOST}:{settings.PORT}")
    uvicorn.run(
        "app:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.ENVIRONMENT.lower() == "development",
        log_config=None
    )
    
