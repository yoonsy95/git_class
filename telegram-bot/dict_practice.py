artists = {
    'artist': {
        'IU': '블루밍',
        '민수': '민수는 혼란스럽다'
    }
}

# 민수 대표곡
# 첫번째 방법
print(artists['artist']['민수'])

# 두번째 방법
print(artists.get('artist').get('민수'))


