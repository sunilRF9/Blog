from .documents import PostDocument
def search(request):
    query = request.GET.get('q')
    res = match(query)
    print(res)
    context = {'queryset':res}
    if res:
        return render(request, 'search_results.html', context=context)
    else:
        return render(request, 'index.html')

def match(query):
    s = PostDocument.search().filter("match", title = query)
    response = s.execute()
    return response


