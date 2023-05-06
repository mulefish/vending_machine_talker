<?php 

$web_host = "https://dispensego.com";
$machine_host = "http://localhost";
$order_id = $argv[1];
$log = "";

$url = $web_host . "/wp-json/dispensgo/v1/order-check/" . $order_id;
$headers = array();
	
$curl = curl_init();

curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($curl, CURLOPT_CUSTOMREQUEST, 'GET');
curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);

curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);

$result = curl_exec($curl);
curl_close($curl);
$json_result = json_decode($result,true);

$valid = isset($json_result['result']) ? $json_result['result'] : false;
if($valid){
	$products = $json_result['products'];
	
	$url = $machine_host . "/avend?action=start";
	$headers = array();
		
	$curl = curl_init();

	curl_setopt($curl, CURLOPT_CUSTOMREQUEST, 'GET');
	curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);

	curl_setopt($curl, CURLOPT_URL, $url);
	curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($curl, CURLOPT_COOKIESESSION, 1);
	curl_setopt($curl, CURLOPT_COOKIEJAR, '');
	curl_setopt($curl, CURLOPT_COOKIEFILE, '');

	$result = curl_exec($curl);
	$log .= date("H:i:s") . " - " . $result . "\n";
	echo $result . "\n";
	
	foreach($products as $p){
		$url = $machine_host . "/avend?action=add&code=" . $p;
		curl_setopt($curl, CURLOPT_URL, $url);
		curl_setopt($curl, CURLOPT_CUSTOMREQUEST, 'GET');

		$result = curl_exec($curl);
		$log .= date("H:i:s") . " - " . $result . "\n";
		echo $result . "\n";
	}
	
	$url = $machine_host . "/avend?action=dispense";
	curl_setopt($curl, CURLOPT_URL, $url);
	curl_setopt($curl, CURLOPT_CUSTOMREQUEST, 'GET');

	$result = curl_exec($curl);
	$log .= date("H:i:s") . " - " . $result . "\n";
	echo $result . "\n";
	
	curl_close($curl);
	
}else{
	$message = isset($json_result['message']) ? $json_result['message'] : $result;
	$log .= date("H:i:s") . " - " . $message . "\n";
	echo $message . "\n";
}

file_put_contents(date("m_d_y") . '.txt', $log.PHP_EOL , FILE_APPEND | LOCK_EX);

?>
