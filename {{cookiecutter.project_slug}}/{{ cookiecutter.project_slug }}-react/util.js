export const cookies = {
  get: (key) => {
      var value = "; " + document.cookie;
      var parts = value.split("; " + key + "=");
      if (parts.length == 2) return parts.pop().split(";").shift();
  }
}
