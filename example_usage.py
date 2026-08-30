from client import VisualDagAgentWorkflowToolChainerClient

def main():
    client = VisualDagAgentWorkflowToolChainerClient()
    res = client.execute_dag_workflow({'nodes': [{'id': 'n1', 'type': 'sentiment_analyzer'}, {'id': 'n2', 'type': 'auto_reply'}], 'edges': [{'from': 'n1', 'to': 'n2'}]})
    print('DAG Agent Chainer: ' + res['dag_execution_id'] + ' (' + str(res['nodes_executed_count']) + ' nodes)')
    print('Latency: ' + str(res['end_to_end_latency_ms']) + 'ms | Checkpoint Recovery: ' + str(res['checkpoint_recovery_available']))
    print('Output: ' + str(res['final_node_response']))
    print('Telemetry: ' + res['dag_execution_telemetry_url'])

if __name__ == '__main__':
    main()
