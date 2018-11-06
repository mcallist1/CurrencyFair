var messageContainer = document.getElementById("message-output");
var btn = document.getElementById('btn')
btn.addEventListener("click", function() {
	var req = new XMLHttpRequest();
	req.open('GET', '/message');
	req.onload = function() {
		var data = JSON.parse(req.responseText);
		renderHTML(data.trade_messages);
	};
	req.send();
});

function renderHTML(data) {
	var table = '<p>';
	table += '<tr>';
	table += '<td  style="font-weight:bold"> Transaction ID </td>';
	table += '<td  style="font-weight:bold"> Selling </td>';
	table += '<td  style="font-weight:bold">  Buying </td>';
	table += '<td  style="font-weight:bold"> Exchange Rate </td>';
	table += '<td  style="font-weight:bold"> Time Placed </td>';
	table += '<td  style="font-weight:bold"> Originating Country </td>';
	table += '</tr>';

	for (var row = 0; row < data.length; row++) {

		table += '<tr>';
		table += '<td>' + escapeHtml(data[row].userId) + '</td>';
		table += '<td>' + escapeHtml(data[row].currencyFrom) + ' '
				+ escapeHtml(data[row].amountSell) + '</td>';
		table += '<td>' + escapeHtml(data[row].currencyTo) + ' '
				+ escapeHtml(data[row].amountBuy) + '</td>';
		table += '<td>' + escapeHtml(data[row].rate) + '</td>';
		table += '<td>' + escapeHtml(data[row].timePlaced) + '</td>';
		table += '<td>' + escapeHtml(data[row].originatingCountry) + '</td>';
		table += '</tr>';
	}
	table += '</p>';

	messageContainer.insertAdjacentHTML('beforeend', table);
}

function escapeHtml(text) {
	if(text && typeof(text) == "string") {
		return text.replace(/&/g, "&amp;"
				).replace(/</g, "&lt;"
				).replace(/>/g, "&gt;"
				).replace(/"/g, "&quot;"
				).replace(/'/g, "&#039;");
	}
	else {
		return text;
	}

}
