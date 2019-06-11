import matplotlib.pyplot as plt
import io
import base64

 
def build_graph(x_coordinates, y_coordinates):
    img = io.BytesIO()
	#plt.style.use('seaborn-whitegrid')
    plt.plot(x_coordinates, y_coordinates,'-ok',linewidth=2,markerfacecolor='white',
         markeredgecolor='gray',
         markeredgewidth=2,markersize=14,color='g')
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(graph_url)