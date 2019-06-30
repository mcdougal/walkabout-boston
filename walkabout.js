
$(document).ready(function() {

    function openModal(photo) {
        var modal = $('#modal');
	var modalPhoto = modal.find('#modal-photo');

	modalPhoto.removeClass("modal-photo-v");
	modalPhoto.removeClass("modal-photo-h");

	modalPhoto.attr("src", photo.attr("src"));

        if (photo.hasClass("photo-v")) {
            modalPhoto.addClass("modal-photo-v");
        }
        else {
	    modalPhoto.addClass("modal-photo-h");
        }

	$("body").addClass("modal-open");

        modal.show();
    }

    function closeModal() {
	$("body").removeClass("modal-open");
        $("#modal").hide();
    }

    $(".photo").click(function(e) {
	openModal($(e.target));
    });

    $("#modal-close").click(function(e) {
	closeModal();
    });

    $(document).keyup(function(e) {
	if (e.which == 27) {
	    closeModal();
	}
    });

});