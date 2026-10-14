(function () {
  function setupBackLink() {
    const backLink = document.querySelector(".project-header__back");
    if (!backLink) return;
    try {
      const savedTab =
        sessionStorage.getItem("portfolioActiveTab") ||
        localStorage.getItem("portfolioActiveTab");
      if (savedTab) {
        backLink.setAttribute("href", "index.html#" + savedTab);
      }
    } catch (e) {}
    backLink.addEventListener("click", (e) => {
      if (
        window.history.length > 1 &&
        document.referrer &&
        document.referrer.includes(window.location.host)
      ) {
        e.preventDefault();
        window.history.back();
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setupBackLink);
  } else {
    setupBackLink();
  }
})();
