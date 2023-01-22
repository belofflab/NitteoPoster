$array = array();
$array['pair_give'] = '12';
$data = wp_remote_post('https://kumicho.pw/api/v1/items', array(
              'headers'     => array('Content-Type' => 'application/json; charset=utf-8'),
              'body'        => json_encode($array),
              'method'      => 'POST',
              'data_format' => 'body',
));
