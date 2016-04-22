#Team l1ghtsab3r

Soumya Sharma - soummyaah
Srishti Sengupta - SrishtiSengupta


We will be creating a generic frontend/backend framework for visualizing the algorithms. This would remove the overhead burden of having to customize visualizations for each algorithm. The backend server would be written in Flask. The front-end would be managed by generic functions written in d3js. We’ll establish a communication protocol between the server and the front-end JS for passing visualization commands and arbitrary log messages to be displayed. The JS would then plugin to these commands and show the visualizations. This would de-couple the front-end service and backend service and allow us to focus on making them work independently. For instance, for a sorting algorithm, the only visualization command that the frontend should support would be a demonstrateSwap(). Because of this decoupling, the server can demonstrate different sorting algorithms without needing the front-end to be tied to it. Another instance would be to create emphasiseEdge() and emphasiseNode() functions on the front-end. This would allow us to explore different traversals and path finding algorithms without having to worry about clean visualization.
