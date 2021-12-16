# Recomendation-Entree-Data-Set
- Using Apriori
- 结果展示：
  ![360截图17620504478241](https://user-images.githubusercontent.com/84648756/146302352-39eab016-94fe-4332-a018-c52e55957348.png)
 - **算法思想：**
    - Support(A) = 包含 A 的记录数量 / Total 记录
    - Conf(A->B) = 包含 A 和 B 的记录数量 / 包含 A 的记录
    - Lift(A->B) = Conf(A->B) / Support(A) = 包含 A 和 B 的记录数量 / Total 记录的数量
    1. 若一个项集是非频繁项集， 那么它的所有超集都是
    2. 非频繁项集，对非频繁项集的根节点进行剪枝，使用递归进行遍历数据集。最小支持度手动设定，通过支持度反映频繁项

  
## 官网数据集介绍
  - This collection contains files related to the Entree system.
  - There are two directories:

    1. data 	- the data files describing restaurants of various cities and a master feature dictionary.
    2. session - session data gathered from the use of the Entree system
---

  There are README files in each directory that describe the specific file formats.

  For more information about the Entree system, see

  Knowledge-based Recommender Systems. To appear in the Encyclopedia of Library and Information Science.
  (http://www.ics.uci.edu/~burke/research/papers/burke-elis-00.pdf.gz, compressed Postscript 870k).

  The Wasabi Personal Shopper: A Case-Based Recommender System. In Proceedings of the 11th National
  Conference on Innovative Applications of Artificial Intelligence, pages 844-849. AAAI, 1999. 
  (http://www.ics.uci.edu/~burke/research/papers/burke-iaai-99.pdf.gz, compressed Postscript 147k).

