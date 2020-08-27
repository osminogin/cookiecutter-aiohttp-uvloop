async def version_middleware(app, handler):
    async def middleware(request):
        response = await handler(request)
        response.headers['X-API-Version'] = app.version
        return response
    return middleware
