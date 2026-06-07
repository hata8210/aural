const ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789";

/**
 * Generates a random ID.
 * Provides a fallback for environments where crypto is not available.
 */
export function nanoid(size = 21): string {
  let id = "";
  const _crypto =
    typeof crypto !== "undefined"
      ? crypto
      : typeof window !== "undefined"
        ? window.crypto
        : undefined;

  if (!_crypto || !_crypto.getRandomValues) {
    for (let i = 0; i < size; i++) {
      id += ALPHABET[(Math.random() * ALPHABET.length) | 0];
    }
    return id;
  }

  const bytes = _crypto.getRandomValues(new Uint8Array(size));
  for (let i = 0; i < size; i++) {
    id += ALPHABET[bytes[i] % ALPHABET.length];
  }
  return id;
}

/**
 * Generates a random UUID (v4).
 * Provides a fallback for non-secure contexts (HTTP) where crypto.randomUUID is not available.
 */
export function randomUUID(): string {
  const _crypto =
    typeof crypto !== "undefined"
      ? crypto
      : typeof window !== "undefined"
        ? window.crypto
        : undefined;

  if (_crypto && typeof _crypto.randomUUID === "function") {
    return _crypto.randomUUID();
  }

  // Fallback using crypto.getRandomValues if available
  if (_crypto && typeof _crypto.getRandomValues === "function") {
    return (([1e7] as any) + -1e3 + -4e3 + -8e3 + -1e11).replace(
      /[018]/g,
      (c: any) =>
        (
          c ^
          (_crypto.getRandomValues(new Uint8Array(1))[0] & (15 >> (c / 4)))
        ).toString(16),
    );
  }

  // Last resort: Math.random (not cryptographically secure)
  return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, (c) => {
    const r = (Math.random() * 16) | 0;
    const v = c === "x" ? r : (r & 0x3) | 0x8;
    return v.toString(16);
  });
}
