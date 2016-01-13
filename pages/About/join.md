title: Join CURB

<p>
<div class="carousel">
  <div><img src="./images/front/1.jpg"></div>
  <div><img src="./images/front/2.jpg"></div>
  <div><img src="./images/front/3.jpg"></div>
  <div><img src="./images/front/4.jpg"></div>
</div>
</p>

<script>
  $(document).ready(function() {
    $('.carousel').slick({
      dots: true,
      autoplay: true,
      arrows: false,
      variableWidth: true,
      adaptiveHeight: true,
      autoplaySpeed: 6000,
    });
  });
</script>

Join our mailing list for research opportunities and the latest CURB events.

<form action="#" method="GET">
  <div class="form-entry">
    <label for="name">Name:</label>
    <input type="text" name="name" id="name">
  </div>
  <div class="form-entry">
    <label for="netid">NetID:</label>
    <input type="text" name="netid" id="netid"><br>
  </div>
  <input type="submit" name="submit" id="submit" value="Sign Up">
</form>
