import os
import networkx as nx
import matplotlib.pyplot as plt


def calculate_pagerank(folder_path):
    files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

    graph = nx.DiGraph()

    # 모든 파일은 서로 연결 되어 있다고 가정
    for file in files:
        graph.add_node(file)

    for file1 in files:
        for file2 in files:
            if file1 != file2:
                graph.add_edge(file1, file2)

    # PageRank 계산
    pagerank_scores = nx.pagerank(graph)

    # 중요도에 따라 파일 목록 정렬
    sorted_files = sorted(pagerank_scores, key=pagerank_scores.get, reverse=True)

    print("텍스트 파일 중요도 순위:")
    for i, file in enumerate(sorted_files, start=1):
        print(f"{i}. {file}: {pagerank_scores[file]}")

    # 결과 시각화
    nx.draw(graph, with_labels=True)
    plt.show()


# 경로
folder_path = '/path/to/your/folder'

# PageRank 계산 및 결과 출력
calculate_pagerank(folder_path)
