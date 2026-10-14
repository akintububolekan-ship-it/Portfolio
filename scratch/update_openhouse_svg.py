def update_openhouse():
    p1 = 'images/Open house/Container.svg'
    with open(p1, 'r', encoding='utf-8') as f:
        content = f.read()
    old_tag1 = '<svg width="668" height="6615" viewBox="0 0 668 6615" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">'
    new_tag1 = '<svg width="640" height="6587.04" viewBox="13.5215 2.25342 640 6587.04" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">'
    if old_tag1 in content:
        content = content.replace(old_tag1, new_tag1, 1)
        content = content.replace('<g filter="url(#filter0_dd_763_113053)">', '<g>', 1)
        with open(p1, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated images/Open house/Container.svg')
    else:
        print('old_tag1 not found in Container.svg')

    p2 = 'images/Open house/Container-1.svg'
    with open(p2, 'r', encoding='utf-8') as f:
        content = f.read()
    old_tag2 = '<svg width="668" height="5255" viewBox="0 0 668 5255" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">'
    new_tag2 = '<svg width="640" height="5227.04" viewBox="13.5215 2.25391 640 5227.04" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">'
    if old_tag2 in content:
        content = content.replace(old_tag2, new_tag2, 1)
        content = content.replace('<g filter="url(#filter0_dd_763_113199)">', '<g>', 1)
        with open(p2, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated images/Open house/Container-1.svg')
    else:
        print('old_tag2 not found in Container-1.svg')

if __name__ == '__main__':
    update_openhouse()
