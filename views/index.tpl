% rebase('base.tpl')
<h1>Twitter Sentiment Analysis</h1>
<form action="/sentiment" method="GET">
	<label for="hashtag">Search for any topic: </label>
	<input type="text" name="hashtag" placeholder="Eg. worldcup2015, rubyconf">
	<input type="submit" value="Go">
</form>
