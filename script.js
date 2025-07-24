// ===============================================
// 目次を自動生成する機能（記事ページでのみ動作）
// ===============================================
function createTableOfContents() {
    const tocList = document.getElementById('toc-list');
    const articleBody = document.querySelector('.article-body');
    
    // 記事ページ以外のページでは、何もしないで終了
    if (!tocList || !articleBody) {
        return;
    }

    const headings = articleBody.querySelectorAll('h2, h3');
    let headingCount = 0;

    headings.forEach(heading => {
        if (heading.parentElement.classList.contains('table-of-contents')) {
            return;
        }

        headingCount++;
        const id = `heading-${headingCount}`;
        heading.id = id;

        const li = document.createElement('li');
        const a = document.createElement('a');
        a.textContent = heading.textContent;
        a.href = `#${id}`;

        if (heading.tagName === 'H3') {
            li.classList.add('toc-h3');
        }

        li.appendChild(a);
        tocList.appendChild(li);
    });
    
    // 目次が1つもなければ、目次セクション自体を非表示に
    if(headingCount === 0) {
        const tocSection = document.querySelector('.table-of-contents');
        if(tocSection) {
            tocSection.style.display = 'none';
        }
    }
}

// ページの読み込み完了時に、上記の目次生成機能を実行
document.addEventListener('DOMContentLoaded', createTableOfContents);