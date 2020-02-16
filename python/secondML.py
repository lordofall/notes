def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)
	
candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
# Write loop to find the ideal tree size from candidate_max_leaf_nodes
best_tree_size = candidate_max_leaf_nodes[0]
mae = get_mae(best_tree_size, train_X, val_X, train_y, val_y) 
for max_leaf_node in candidate_max_leaf_nodes:
    temp = get_mae(max_leaf_node, train_X, val_X, train_y, val_y)
    if temp < mae:
        mae = temp
        best_tree_size = max_leaf_node
		
# Fill in argument to make optimal size and uncomment
final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state=1)

# fit the final model and uncomment the next two lines
final_model.fit(X, y)